from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.sm7 import (
    lazy_passive,
)
from spirit.game.card_effects.attacks_common import self_energy_discard_attack

card = PokemonCardDef(
    guid="ba81e28a-ce77-5e8a-90ba-60b52eae308f",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slaking.Name",
    display_name="Slaking",
    searchable_by=["Slaking", "Stage 2", "Slaking"],
    subtypes=["Stage 2"],
    collector_number=115,
    set_code="SM7",
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vigoroth.Name",
    family_id=287,
    abilities=[
        Ability(
            title="Lazy",
            game_text="As long as this Pok\u00e9mon is your Active Pok\u00e9mon, your opponent's Pok\u00e9mon in play have no Abilities, except for Lazy.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=lazy_passive,
        ),
        Attack(
            title="Critical Move",
            game_text="Discard an Energy from this Pok\u00e9mon. It can't attack during your next turn.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=160,
            effect=self_energy_discard_attack(count=1),
            locks_next_turn=True,
        ),
    ],
)