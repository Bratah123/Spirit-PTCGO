from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ed6b43c2-d914-59d9-a17c-dba4c5b9ad99",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spiritomb.Name",
    display_name="Spiritomb",
    searchable_by=["Spiritomb", "Basic", "Spiritomb"],
    subtypes=["Basic"],
    collector_number=117,
    set_code="SWSH11",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=442,
    abilities=[
        Ability(
            title="Cursed Message",
            game_text="If this Pok\u00e9mon is Knocked Out by damage from an attack from your opponent's Pok\u00e9mon, search your deck for a card and put it into your hand. Then, shuffle your deck.",
            effect=unimplemented,
        ),
        Attack(
            title="Chain of Spirits",
            game_text="This attack does 60 more damage for each Spiritomb in your discard pile.",
            cost={PokemonTypes.DARKNESS: 2},
            damage=10,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)