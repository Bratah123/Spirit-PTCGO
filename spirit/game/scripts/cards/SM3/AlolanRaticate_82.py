from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_or_nothing
from spirit.game.card_effects.sm3 import enhanced_fang


card = PokemonCardDef(
    guid="e13f7ae3-bc8e-57d5-94fa-2d77a34a8cc7",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanRaticate.Name",
    display_name="Alolan Raticate",
    searchable_by=["Alolan Raticate", "Stage 1", "AlolanRaticate"],
    subtypes=["Stage 1"],
    collector_number=82,
    set_code="SM3",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanRattata.Name",
    family_id=19,
    abilities=[
        Attack(
            title="Enhanced Fang",
            game_text="If this Pok\u00e9mon has a Pok\u00e9mon Tool card attached to it, this attack does 50 more damage.",
            cost={},
            damage=10,
            damage_operator="+",
            effect=enhanced_fang,
        ),
        Attack(
            title="Hyper Fang",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=60,
            # STUB: attack effect not implemented
            effect=flip_or_nothing(),
        ),
    ],
)
