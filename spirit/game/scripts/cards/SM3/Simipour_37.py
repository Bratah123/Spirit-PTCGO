from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm3 import aqua_reflect

card = PokemonCardDef(
    guid="87e8242e-f083-5fca-8b2a-950f028a5b71",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Simipour.Name",
    display_name="Simipour",
    searchable_by=["Simipour", "Stage 1", "Simipour"],
    subtypes=["Stage 1"],
    collector_number=37,
    set_code="SM3",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Panpour.Name",
    family_id=515,
    abilities=[
        Attack(
            title="Scratch",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Aqua Reflect",
            game_text="Move a Water Energy from this Pok\u00e9mon to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=aqua_reflect,
        ),
    ],
)
