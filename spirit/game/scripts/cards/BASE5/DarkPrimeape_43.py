from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ecard import FrenzyPassive


card = PokemonCardDef(
    guid="d034d073-5446-5d3e-8b8c-0b2cfe55a37e",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkPrimeape.Name",
    display_name="Dark Primeape",
    searchable_by=["Dark Primeape", "Stage 1", "DarkPrimeape"],
    subtypes=["Stage 1"],
    collector_number=43,
    set_code="BASE5",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Mankey.Name",
    family_id=56,
    abilities=[
        Ability(
            title="Frenzy",
            game_text="If Dark Primeape does any damage while it's Confused (even to itself), it does 30 more damage.",
            ability_type=AbilityTypes.POKE_POWER,
            passive=FrenzyPassive(),
        ),
        Attack(
            title="Frenzied Attack",
            game_text="Dark Primeape is now Confused (after doing damage).",
            cost={PokemonTypes.FIGHTING: 2},
            damage=40,
            effect=condition_attack(self_conditions=(SpecialConditions.CONFUSED,)),
        ),
    ],
)
