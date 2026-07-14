from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import protect_next_turn

card = PokemonCardDef(
    guid="7cdea712-6b10-54e3-a88a-c9cf360e8c0a",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianSliggoo.Name",
    display_name="Hisuian Sliggoo",
    searchable_by=["Hisuian Sliggoo", "Stage 1", "HisuianSliggoo"],
    subtypes=["Stage 1"],
    collector_number=133,
    set_code="SWSH11",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Goomy.Name",
    family_id=704,
    abilities=[
        Attack(
            title="Rigidify",
            game_text="During your opponent's next turn, this Pok\u00e9mon takes 50 less damage from attacks (after applying Weakness and Resistance).",
            cost={},
            effect=protect_next_turn(reduce=50),
        ),
        Attack(
            title="Gentle Slap",
            cost={PokemonTypes.WATER: 1, PokemonTypes.METAL: 1},
            damage=40,
        ),
    ],
)