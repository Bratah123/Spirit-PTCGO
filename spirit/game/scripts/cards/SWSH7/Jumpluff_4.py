from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9d667fa8-c4d9-5169-9468-14487da4549c",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jumpluff.Name",
    display_name="Jumpluff",
    searchable_by=["Jumpluff", "Stage 2", "Rapid Strike", "Jumpluff"],
    subtypes=["Stage 2", "Rapid Strike"],
    collector_number=4,
    set_code="SWSH7",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Skiploom.Name",
    family_id=187,
    abilities=[
        Ability(
            title="Fluffy Barrage",
            game_text="This Pok\u00e9mon may attack twice each turn. If the first attack Knocks Out your opponent's Active Pok\u00e9mon, you may attack again after your opponent chooses a new Active Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Spinning Attack",
            cost={PokemonTypes.GRASS: 1},
            damage=60,
        ),
    ],
)