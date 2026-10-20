from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.trainers import is_energy_card
from spirit.game.card_effects.attacks_common import damage_per, count_energy


async def _meddling(ctx):
    """Attach 3 Energy cards from your opponent's discard pile to their
    Pokemon in any way you like."""
    for _ in range(3):
        cards = [c for c in ctx.discard_pile(ctx.opponent_id) if is_energy_card(c)]
        targets = ctx.opponent_pokemon_in_play()
        if not cards or not targets:
            return
        picks = await ctx.choose_cards(cards, 1, minimum=1, prompt="Choose an Energy card to attach")
        if not picks:
            return
        target = targets[0] if len(targets) == 1 else await ctx.choose_pokemon(
            targets, "Attach it to which of your opponent's Pokémon?")
        await ctx.attach_energy(picks[0], target or targets[0])


card = PokemonCardDef(
    guid="acad5162-543c-5d4d-91ce-af0a3ad00fb1",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jellicent.Name",
    display_name="Jellicent",
    searchable_by=["Jellicent", "Stage 1", "Jellicent"],
    subtypes=["Stage 1"],
    collector_number=21,
    set_code="XY4",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Frillish.Name",
    family_id=592,
    abilities=[
        Attack(
            title="Meddling",
            game_text="Attach 3 Energy cards from your opponent's discard pile to his or her Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.WATER: 1},
            effect=_meddling,
        ),
        Attack(
            title="Ensnaring Spray",
            game_text="This attack does 10 more damage for each Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=damage_per(count_energy('defender'), 10, base=50),
        ),
    ],
)