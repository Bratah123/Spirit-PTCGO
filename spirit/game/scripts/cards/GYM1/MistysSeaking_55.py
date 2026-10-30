from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import mud_splash


card = PokemonCardDef(
    guid="29df19e3-2103-5eb9-a0ef-bc75fcb85bf0",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MistysSeaking.Name",
    display_name="Misty's Seaking",
    searchable_by=["Misty's Seaking", "Stage 1", "MistysSeaking"],
    subtypes=["Stage 1"],
    collector_number=55,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.MistysGoldeen.Name",
    family_id=118,
    abilities=[
        Attack(
            title="Horn Attack",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
        Attack(
            title="Mud Splash",
            game_text="If your opponent has any Benched Pok\u00e9mon, choose 1 of them and flip a coin. If heads, this attack does 10 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 2},
            damage=30,
            effect=mud_splash,
        ),
    ],
)
