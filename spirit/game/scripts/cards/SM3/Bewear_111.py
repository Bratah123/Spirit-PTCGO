from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.sm3 import mix_up


card = PokemonCardDef(
    guid="c9019459-8be3-5101-9d5d-d19462f63199",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bewear.Name",
    display_name="Bewear",
    searchable_by=["Bewear", "Stage 1", "Bewear"],
    subtypes=["Stage 1"],
    collector_number=111,
    set_code="SM3",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Stufful.Name",
    family_id=759,
    abilities=[
        Attack(
            title="Mix-Up",
            game_text="Flip a coin. If heads, discard the top 3 cards of your opponent's deck.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=mix_up,
        ),
        Attack(
            title="Tantrum",
            game_text="This Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=120,
            # STUB: attack effect not implemented
            effect=condition_attack(self_conditions=(SpecialConditions.CONFUSED,)),
        ),
    ],
)
