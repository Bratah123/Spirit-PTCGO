from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d16443f5-fbbd-5dc0-9558-c703387cc38a",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RayquazaV.Name",
    display_name="Rayquaza V",
    searchable_by=["Rayquaza V", "Basic", "V", "Rapid Strike", "RayquazaV"],
    subtypes=["Basic", "V", "Rapid Strike"],
    collector_number=194,
    set_code="SWSH7",
    rarity=Rarities.RareUltra,
    hp=210,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    family_id=384,
    abilities=[
        Attack(
            title="Dragon Pulse",
            game_text="Discard the top 2 cards of your deck.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=40,
            effect=unimplemented,
        ),
        Attack(
            title="Spiral Burst",
            game_text="You may discard up to 2 basic Fire Energy or up to 2 basic Lightning Energy from this Pok\u00e9mon. This attack does 80 more damage for each card you discarded in this way.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.LIGHTNING: 1},
            damage=20,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)