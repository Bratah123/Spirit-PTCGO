from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import self_energy_discard_attack
from spirit.game.card_effects.sm5 import chaotic_star

card = PokemonCardDef(
    guid="f6b0e098-bcc1-5e0e-b063-388ca18fff76",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GiratinaPrismStar.Name",
    display_name="Giratina {*}",
    searchable_by=["Giratina {*}", "Basic", "Prism Star", "GiratinaPrismStar"],
    subtypes=["Basic", "Prism Star"],
    collector_number=58,
    set_code="SM5",
    rarity=Rarities.Prism,
    hp=160,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=487,
    abilities=[
        Ability(
            title="Chaotic Star",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench during your turn, you may attach 2 Psychic Energy cards from your hand to it.",
            ability_type=AbilityTypes.POKE_ABILITY,
            effect=chaotic_star,
            trigger=Triggers.ON_PLAY,
        ),
        Attack(
            title="Crisis Dive",
            game_text="Discard 2 Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 4},
            damage=160,
            # STUB: attack effect not implemented
            effect=self_energy_discard_attack(count=2),
        ),
    ],
)