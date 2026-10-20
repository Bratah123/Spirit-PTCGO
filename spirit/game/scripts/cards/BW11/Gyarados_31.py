from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per


def _prizes_both(ctx):
    """Prize cards both players have taken."""
    return ctx.prizes_taken(ctx.player_id) + ctx.prizes_taken(ctx.opponent_id)


card = PokemonCardDef(
    guid="3649d456-fa0b-520e-a415-424c9cdb3aef",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gyarados.Name",
    display_name="Gyarados",
    searchable_by=["Gyarados", "Stage 1", "Gyarados"],
    subtypes=["Stage 1"],
    collector_number=31,
    set_code="BW11",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Magikarp.Name",
    family_id=129,
    abilities=[
        Attack(
            title="Howling Rampage",
            game_text="Does 20 damage times the number of Prize cards both players have taken.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=damage_per(_prizes_both, 20),
        ),
        Attack(
            title="Hydro Splash",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 3},
            damage=120,
        ),
    ],
)