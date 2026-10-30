from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import AbilityTypes, PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.ex import free_flight_passive
from spirit.game.card_effects.attacks_common import snipe_attack

card = PokemonCardDef(
    guid="394c606d-8887-5606-b4c5-d63a2f48f2c3",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Fearow.Name",
    display_name="Fearow",
    searchable_by=["Fearow", "Stage 1", "Fearow"],
    subtypes=["Stage 1"],
    collector_number=24,
    set_code="EX6",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Spearow.Name",
    family_id=21,
    abilities=[
        Ability(
            title="Free Flight",
            game_text="If Fearow has no Energy attached to it, Fearow's Retreat Cost is 0.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=free_flight_passive(),
        ),
        Attack(
            title="Shot Air",
            game_text="Does 20 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            effect=snipe_attack(20),
        ),
        Attack(
            title="Drill Peck",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
        ),
    ],
)