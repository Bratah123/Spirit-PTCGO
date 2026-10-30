from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import AbilityTypes, PokemonStage, PokemonTypes, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ex import family_bonds_passive, power_lariat


card = PokemonCardDef(
    guid="c8db9980-1fa1-5b87-aeb9-a56720319bf7",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nidoqueen.Name",
    display_name="Nidoqueen",
    searchable_by=["Nidoqueen", "Stage 2", "Nidoqueen"],
    subtypes=["Stage 2"],
    collector_number=9,
    set_code="EX6",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nidorina.Name",
    family_id=29,
    abilities=[
        Ability(
            title="Family Bonds",
            game_text="As long as Nidoqueen is in play, the Retreat Cost for Nidoran \u2640, Nidorina, Nidoran \u2642, Nidorino and Nidoking is 0.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=family_bonds_passive(),
        ),
        Attack(
            title="Toxic",
            game_text="The Defending Pok\u00e9mon is now Poisoned. Put 2 damage counters instead of 1 on the Defending Pok\u00e9mon between turns.",
            cost={PokemonTypes.GRASS: 1},
            effect=condition_attack(SpecialConditions.POISONED, counters=2),
        ),
        Attack(
            title="Power Lariat",
            game_text="Does 40 damage plus 10 more damage for each Evolved Pok\u00e9mon you have in play.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            effect=power_lariat(40, 10),
        ),
    ],
)