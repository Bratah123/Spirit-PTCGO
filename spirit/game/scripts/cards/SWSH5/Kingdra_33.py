from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="cd9c1d5b-be03-5187-8910-c7d13d119a83",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kingdra.Name",
    display_name="Kingdra",
    searchable_by=["Kingdra", "Stage 2", "Kingdra"],
    subtypes=["Stage 2"],
    collector_number=33,
    set_code="SWSH5",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Seadra.Name",
    family_id=116,
    abilities=[
        Ability(
            title="Deep Sea King",
            game_text="When your Active Pok\u00e9mon is Knocked Out by damage from an attack from your opponent's Pok\u00e9mon, you may move any amount of Water Energy from that Pok\u00e9mon to this Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Aqua Burst",
            game_text="This attack does 40 damage for each Water Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1},
            damage=40,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)