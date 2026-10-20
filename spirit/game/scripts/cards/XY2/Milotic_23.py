from spirit.game.data_utils import Activations, PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.content.definitions import def_for


def _not_ex(pokemon):
    return "EX" not in (getattr(def_for(pokemon.archetype_id), "subtypes", None) or [])


async def _energy_grace(ctx):
    """Knock Out this Pokemon. If you do, attach 3 basic Energy from your
    discard pile to 1 of your Pokemon (excluding Pokemon-EX)."""
    me = ctx.source
    if not await ctx.knock_out(me):
        return
    targets = [p for p in ctx.my_pokemon_in_play() if p is not me and _not_ex(p)]
    cards = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
    if not targets or not cards:
        return
    picks = await ctx.choose_cards(cards, 3, minimum=min(3, len(cards)),
                                   prompt="Choose 3 basic Energy cards to attach")
    if not picks:
        return
    target = targets[0] if len(targets) == 1 else await ctx.choose_pokemon(
        targets, "Choose a Pokémon (not a Pokémon-EX) to attach them to")
    for card in picks:
        await ctx.attach_energy(card, target or targets[0])


card = PokemonCardDef(
    guid="303a029e-e197-520e-b9ea-561f460685e3",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Milotic.Name",
    display_name="Milotic",
    searchable_by=["Milotic", "Stage 1", "Milotic"],
    subtypes=["Stage 1"],
    collector_number=23,
    set_code="XY2",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Feebas.Name",
    family_id=349,
    abilities=[
        Ability(
            title="Energy Grace",
            game_text="Once during your turn (before your attack) you may Knock Out this Pok\u00e9mon. If you do, attach 3 basic Energy from your discard pile to 1 of your Pok\u00e9mon (excluding Pok\u00e9mon-EX).",
            activation=Activations.ONCE_PER_TURN,
            effect=_energy_grace,
        ),
        Attack(
            title="Waterfall",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)