from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if, has_damage


card = PokemonCardDef(
    guid="e4e8f995-609f-54f6-ba44-f4efbe5b1c62",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nidoran.Name",
    display_name="Nidoran ♂",
    searchable_by=["Nidoran \u2642", "Basic", "Nidoran"],
    subtypes=["Basic"],
    collector_number=43,
    set_code="BW9",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=32,
    abilities=[
        Attack(
            title="Hit Back",
            game_text="If this Pok\u00e9mon has no damage counters on it, this attack does nothing.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            effect=bonus_if(has_damage('self'), 0, else_nothing=True),
        ),
    ],
)