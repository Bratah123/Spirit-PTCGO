from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm5 import psychic_60_plus
from spirit.game.card_effects.attacks_common import self_energy_discard_attack


card = PokemonCardDef(
    guid="0c8b890b-78dc-589c-99ac-9e0a046d183d",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Deoxys.Name",
    display_name="Deoxys",
    searchable_by=["Deoxys", "Basic", "Deoxys"],
    subtypes=["Basic"],
    collector_number=67,
    set_code="SM7",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=386,
    abilities=[
        Attack(
            title="Psychic",
            game_text="This attack does 20 more damage times the amount of Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=psychic_60_plus,
        ),
        Attack(
            title="Power Blast",
            game_text="Discard an Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            # STUB: attack effect not implemented
            effect=self_energy_discard_attack(count=1),
        ),
    ],
)