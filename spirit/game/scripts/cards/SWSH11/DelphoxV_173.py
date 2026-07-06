from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="fa35628f-a394-5e28-83d8-6d0bdb8648c1",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DelphoxV.Name",
    display_name="Delphox V",
    searchable_by=["Delphox V", "Basic", "V", "DelphoxV"],
    subtypes=["Basic", "V"],
    collector_number=173,
    set_code="SWSH11",
    rarity=Rarities.RareUltra,
    hp=210,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=655,
    abilities=[
        Attack(
            title="Eerie Glow",
            game_text="Your opponent's Active Pok\u00e9mon is now Burned and Confused.",
            cost={PokemonTypes.FIRE: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Magical Fire",
            game_text="Put 2 Energy attached to this Pok\u00e9mon in the Lost Zone. This attack also does 120 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=unimplemented,
        ),
    ],
)