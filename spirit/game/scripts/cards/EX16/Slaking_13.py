from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import (
    attached_basic_energy_at_least,
    discard_basic_energy_attack,
    lock_own_attacks,
    opponent_poke_power_lock,
)


card = PokemonCardDef(
    guid="13f914d3-3230-584b-a478-050420db7aec",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slaking.Name",
    display_name="Slaking",
    searchable_by=["Slaking", "Stage 2", "Slaking"],
    subtypes=["Stage 2"],
    collector_number=13,
    set_code="EX16",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vigoroth.Name",
    family_id=287,
    abilities=[
        Ability(
            title="Lazy",
            game_text="As long as Slaking is your Active Pok\u00e9mon, your opponent's Pok\u00e9mon can't use any Pok\u00e9-Powers.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=opponent_poke_power_lock(),
        ),
        Attack(
            title="Critical Move",
            game_text="Discard a basic Energy card attached to Slaking or this attack does nothing. Slaking can't attack during your next turn.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=100,
            condition=attached_basic_energy_at_least(1),
            effect=discard_basic_energy_attack(1, also=lock_own_attacks),
        ),
    ],
)
