from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4c3869cf-bc37-5c8b-ae22-7a5d5ea4e075",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LaprasV.Name",
    display_name="Lapras V",
    searchable_by=["Lapras V", "Basic", "V", "LaprasV"],
    subtypes=["Basic", "V"],
    collector_number=189,
    set_code="SWSH1",
    rarity=Rarities.RareUltra,
    hp=210,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=131,
    abilities=[
        Attack(
            title="Body Surf",
            game_text="Attach a Water Energy card from your hand to this Pok\u00e9mon. If you do, switch it with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Ocean Loop",
            game_text="Put 2 Water Energy attached to this Pok\u00e9mon into your hand.",
            cost={PokemonTypes.WATER: 3, PokemonTypes.COLORLESS: 1},
            damage=210,
            effect=unimplemented,
        ),
    ],
)