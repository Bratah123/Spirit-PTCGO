from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f9499785-b8b2-5571-ac3b-56b019a23377",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.NoivernV.Name",
    display_name="Noivern V",
    searchable_by=["Noivern V", "Basic", "V", "NoivernV"],
    subtypes=["Basic", "V"],
    collector_number=117,
    set_code="SWSH7",
    rarity=Rarities.RareHoloV,
    hp=200,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    family_id=715,
    abilities=[
        Attack(
            title="Boomburst",
            game_text="This attack does 20 damage to each of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Synchro Loud",
            game_text="If you have the same number of cards in your hand as your opponent, this attack does 120 more damage.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.DARKNESS: 1},
            damage=60,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)