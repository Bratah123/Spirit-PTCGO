from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ccde68b7-8315-5808-9efb-b4ba23242fa8",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Qwilfish.Name",
    display_name="Qwilfish",
    searchable_by=["Qwilfish", "Basic", "Single Strike", "Qwilfish"],
    subtypes=["Basic", "Single Strike"],
    collector_number=101,
    set_code="SWSH6",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=211,
    abilities=[
        Ability(
            title="Bursting Needles",
            game_text="If this Pok\u00e9mon is in the Active Spot and is Knocked Out by damage from an attack from your opponent's Pok\u00e9mon, put 6 damage counters on the Attacking Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Poison Jab",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=unimplemented,
        ),
    ],
)