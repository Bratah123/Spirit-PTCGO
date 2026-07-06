from spirit.game.card_effects.pokemon import MysteriousNestPassive
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="294dcbed-7729-5d2d-bee6-0f911544a3cf",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dunsparce.Name",
    display_name="Dunsparce",
    searchable_by=["Dunsparce", "Basic", "Dunsparce"],
    subtypes=["Basic"],
    collector_number=207,
    set_code="SWSH8",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=206,
    abilities=[
        Ability(
            title="Mysterious Nest",
            game_text="Colorless Pokémon in play (both yours and your opponent's) have no Weakness.",
            passive=MysteriousNestPassive(),
        ),
        Attack(
            title="Rollout",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
