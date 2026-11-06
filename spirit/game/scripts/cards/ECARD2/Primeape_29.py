from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import (
    damage_counters_on, damage_per, recoil_attack,
)
from spirit.game.card_effects.support_common import opponent_switches


card = PokemonCardDef(
    guid="3a19d9fe-cfd3-53e9-a721-c65aa0b67499",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Primeape.Name",
    display_name="Primeape",
    searchable_by=["Primeape", "Stage 1", "Primeape"],
    subtypes=["Stage 1"],
    collector_number=29,
    set_code="ECARD2",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Mankey.Name",
    family_id=56,
    abilities=[
        Attack(
            title="Karate Chop",
            game_text="Damage from this attack is reduced by 10 for each damage counter on Primeape.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator="-",
            effect=damage_per(damage_counters_on("self"), -10, base=40),
        ),
        Attack(
            title="Sudden Charge",
            game_text="Primeape does 10 damage to itself. Then, your opponent switches the Defending Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon, if any.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=recoil_attack(10, also=opponent_switches),
        ),
    ],
)
