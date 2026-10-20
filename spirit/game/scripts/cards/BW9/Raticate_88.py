from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import is_team_plasma_card, is_pokemon_card, is_trainer_card
from spirit.game.card_effects.pokemon import is_energy_card


async def _transfer_junk(ctx):
    """Put a Team Plasma Pokemon, a Team Plasma Trainer card and a Team Plasma
    Energy card from your discard pile into your hand."""
    groups = [
        (lambda c: is_team_plasma_card(c) and is_pokemon_card(c), "Choose a Team Plasma Pokémon"),
        (lambda c: is_team_plasma_card(c) and is_trainer_card(c), "Choose a Team Plasma Trainer card"),
        (lambda c: is_team_plasma_card(c) and is_energy_card(c), "Choose a Team Plasma Energy card"),
    ]
    picked = []
    for pred, prompt in groups:
        pool = [c for c in ctx.discard_pile() if pred(c)]
        if pool:
            picked += await ctx.choose_cards(pool, 1, minimum=1, prompt=prompt) or []
    if picked:
        await ctx.put_in_hand(picked, reveal=True)


card = PokemonCardDef(
    guid="11a3c887-5149-598d-8666-bbf36100f77a",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Raticate.Name",
    display_name="Raticate",
    searchable_by=["Raticate", "Stage 1", "Team Plasma", "Raticate"],
    subtypes=["Stage 1", "Team Plasma"],
    collector_number=88,
    set_code="BW9",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rattata.Name",
    family_id=19,
    abilities=[
        Attack(
            title="Transfer Junk",
            game_text="Put a Team Plasma Pok\u00e9mon, a Team Plasma Trainer card, and a Team Plasma Energy card from your discard pile into your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_transfer_junk,
        ),
        Attack(
            title="Bite",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)