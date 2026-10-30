from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ecard import poison_power


card = PokemonCardDef(
    guid="c47d79d6-99a6-56c9-b852-2ea555b9bb3d",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.KogasArbok.Name",
    display_name="Koga's Arbok",
    searchable_by=["Koga's Arbok", "Stage 1", "KogasArbok"],
    subtypes=["Stage 1"],
    collector_number=25,
    set_code="GYM2",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.KogasEkans.Name",
    family_id=23,
    abilities=[
        Attack(
            title="Poison Buildup",
            game_text="Koga's Arbok is now Poisoned.",
            cost={PokemonTypes.GRASS: 1},
            effect=condition_attack(self_conditions=(SpecialConditions.POISONED,)),
        ),
        Attack(
            title="Poison Power",
            game_text="If Koga's Arbok is Poisoned, this attack's base damage is 40 instead of 20 and the Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.GRASS: 2},
            damage=20,
            effect=poison_power,
        ),
    ],
)
