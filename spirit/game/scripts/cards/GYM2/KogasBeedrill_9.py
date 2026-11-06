from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ecard import leek_slap, leek_slap_available


card = PokemonCardDef(
    guid="53f3db44-fc53-55c5-a869-557728400cee",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.KogasBeedrill.Name",
    display_name="Koga's Beedrill",
    searchable_by=["Koga's Beedrill", "Stage 2", "KogasBeedrill"],
    subtypes=["Stage 2"],
    collector_number=9,
    set_code="GYM2",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.KogasKakuna.Name",
    family_id=13,
    abilities=[
        Attack(
            title="Nerve Poison",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed and Poisoned.",
            cost={PokemonTypes.GRASS: 2},
            damage=20,
            effect=condition_attack(SpecialConditions.PARALYZED, SpecialConditions.POISONED, flip=True),
        ),
        Attack(
            title="Hyper Needle",
            game_text="Flip a coin. If tails, this attack does nothing. Either way, you can't use this attack again as long as Koga's Beedrill stays in play (even putting Koga's Beedrill on the Bench won't let you use it again).",
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
            condition=leek_slap_available,
            effect=leek_slap,
        ),
    ],
)
