from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import rock_crush

card = PokemonCardDef(
    guid="ae3808fb-1e9e-5348-b53a-260ab74a0a3c",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AerodactylV.Name",
    display_name="Aerodactyl V",
    searchable_by=["Aerodactyl V", "Basic", "V", "AerodactylV"],
    subtypes=["Basic", "V"],
    collector_number=92,
    set_code="SWSH11",
    rarity=Rarities.RareHoloV,
    hp=210,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=142,
    abilities=[
        Attack(
            title="Bite",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
        Attack(
            title="Rock Crush",
            game_text="Discard an Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=rock_crush,
        ),
    ],
)
