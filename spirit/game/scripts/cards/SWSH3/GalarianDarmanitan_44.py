from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5f1aa1ff-0343-5236-955f-c6ba461d7f7a",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianDarmanitan.Name",
    display_name="Galarian Darmanitan",
    searchable_by=["Galarian Darmanitan", "Stage 1", "GalarianDarmanitan"],
    subtypes=["Stage 1"],
    collector_number=44,
    set_code="SWSH3",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianDarumaka.Name",
    family_id=554,
    abilities=[
        Attack(
            title="Blizzard",
            game_text="This attack also does 10 damage to each of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=unimplemented,
        ),
        Attack(
            title="Crushing Headbutt",
            game_text="During your next turn, this Pok\u00e9mon can't use Crushing Headbutt.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=170,
            effect=unimplemented,
        ),
    ],
)