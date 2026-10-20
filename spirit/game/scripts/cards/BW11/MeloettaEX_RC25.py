from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import damage_per, count_in_play, has_attack_titled, condition_attack


card = PokemonCardDef(
    guid="eb3e99b5-92a5-522f-9ec8-d28c1bb79283",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MeloettaEX.Name",
    display_name="Meloetta-EX",
    searchable_by=["Meloetta-EX", "Basic", "EX", "MeloettaEX"],
    subtypes=["Basic", "EX"],
    collector_number=140,
    set_code="BW11",
    rarity=Rarities.RareUltra,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=648,
    abilities=[
        Attack(
            title="Brilliant Voice",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Asleep. If tails, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=condition_attack(SpecialConditions.ASLEEP, flip=True, tails_conditions=(SpecialConditions.CONFUSED,)),
        ),
        Attack(
            title="Round",
            game_text="Does 30 damage times the number of your Pok\u00e9mon that have the Round attack.",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=30,
            damage_operator="x",
            effect=damage_per(count_in_play('mine', has_attack_titled('Round')), 30),
        ),
    ],
)