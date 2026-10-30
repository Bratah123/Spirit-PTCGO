from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes, SpecialConditions
from spirit.game.card_effects.attacks_common import (
    condition_attack, damage_per, damage_counters_on,
)
from spirit.game.card_effects.ex import burning_aura


card = PokemonCardDef(
    guid="0875485a-8b33-5c49-ac3b-8cf7497cbc74",
    key="NP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Typhlosion.Name",
    display_name="Typhlosion",
    searchable_by=["Typhlosion", "Stage 2", "Typhlosion"],
    subtypes=["Stage 2"],
    collector_number=34,
    set_code="NP",
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Quilava.Name",
    family_id=157,
    abilities=[
        Ability(
            title="Burning Aura",
            game_text="As long as Typhlosion is your Active Pok\u00e9mon, put 1 damage counter on each Active Pok\u00e9mon (both yours and your opponent's) between turns.",
            ability_type=AbilityTypes.POKE_BODY,
            trigger=Triggers.BETWEEN_TURNS,
            effect=burning_aura(1),
        ),
        Attack(
            title="Flickering Flames",
            game_text="The Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
        Attack(
            title="Rage",
            game_text="Does 50 damage plus 10 more damage for each damage counter on Typhlosion.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=damage_per(damage_counters_on("self"), per=10, base=50),
        ),
    ],
)
