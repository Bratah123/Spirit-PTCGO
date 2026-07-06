from spirit.game.card_effects.pokemon import final_dig
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="208661c3-d082-5d6c-8a6e-2bd52c3d0edb",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dunsparce.Name",
    display_name="Dunsparce",
    searchable_by=["Dunsparce", "Basic", "Dunsparce"],
    subtypes=["Basic"],
    collector_number=137,
    set_code="SWSH3",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=206,
    abilities=[
        Ability(
            title="Final Dig",
            game_text="If this Pok\u00e9mon is Knocked Out by damage from an attack from your opponent's Pok\u00e9mon, discard the top 2 cards of your opponent's deck.",
            trigger=Triggers.ON_KNOCKED_OUT,
            effect=final_dig,
        ),
        Attack(
            title="Ram",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)