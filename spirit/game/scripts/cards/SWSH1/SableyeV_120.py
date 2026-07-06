from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="59eb1d89-ad28-5923-8d84-e867c63358cf",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SableyeV.Name",
    display_name="Sableye V",
    searchable_by=["Sableye V", "Basic", "V", "SableyeV"],
    subtypes=["Basic", "V"],
    collector_number=120,
    set_code="SWSH1",
    rarity=Rarities.RareHoloV,
    hp=170,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=302,
    abilities=[
        Attack(
            title="Lode Search",
            game_text="Put a Trainer card from your discard pile into your hand.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Crazy Claws",
            game_text="This attack does 60 more damage for each damage counter on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 2},
            damage=10,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)