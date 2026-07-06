from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d86ebf4c-10b8-55ef-bbd8-43f951be8f46",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DragoniteV.Name",
    display_name="Dragonite V",
    searchable_by=["Dragonite V", "Basic", "V", "DragoniteV"],
    subtypes=["Basic", "V"],
    collector_number=191,
    set_code="SWSH7",
    rarity=Rarities.RareUltra,
    hp=230,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    family_id=149,
    abilities=[
        Attack(
            title="Shred",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=unimplemented,
        ),
        Attack(
            title="Dragon Gale",
            game_text="This attack also does 20 damage to each of your Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.LIGHTNING: 1},
            damage=250,
            effect=unimplemented,
        ),
    ],
)