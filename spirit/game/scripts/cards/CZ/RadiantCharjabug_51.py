from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b6f25036-ac03-5190-ba5e-f4f448c4528c",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RadiantCharjabug.Name",
    display_name="Radiant Charjabug",
    searchable_by=["Radiant Charjabug", "Basic", "Radiant", "RadiantCharjabug"],
    subtypes=["Basic", "Radiant"],
    collector_number=51,
    set_code="CZ",
    rarity=Rarities.RareRadiant,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=737,
    abilities=[
        Ability(
            title="Shocking Block",
            game_text="Whenever any player attaches an Energy card from their hand to 1 of their Pok\u00e9mon V, put 2 damage counters on that Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Linear Attack",
            game_text="This attack does 30 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=unimplemented,
        ),
    ],
)