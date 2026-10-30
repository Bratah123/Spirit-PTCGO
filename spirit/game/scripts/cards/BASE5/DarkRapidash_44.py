from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import flame_pillar


card = PokemonCardDef(
    guid="3ab8a9c6-2017-550f-9442-dbf43021fdb2",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkRapidash.Name",
    display_name="Dark Rapidash",
    searchable_by=["Dark Rapidash", "Stage 1", "DarkRapidash"],
    subtypes=["Stage 1"],
    collector_number=44,
    set_code="BASE5",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ponyta.Name",
    family_id=77,
    abilities=[
        Attack(
            title="Rear Kick",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
        Attack(
            title="Flame Pillar",
            game_text="You may discard 1 Fire Energy card attached to Dark Rapidash when you use this attack. If you do and if your opponent has any Benched Pok\u00e9mon, choose 1 of them and this attack does 10 damage to it. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIRE: 2},
            damage=30,
            effect=flame_pillar,
        ),
    ],
)
