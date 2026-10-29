from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.dm import (
    dragon_guard_passive,
)

card = PokemonCardDef(
    guid="5c9456db-ca34-55a6-8277-6dadca057687",
    key="DM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flygon.Name",
    display_name="Flygon",
    searchable_by=["Flygon", "Stage 2", "Flygon"],
    subtypes=["Stage 2"],
    collector_number=39,
    set_code="DM",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FAIRY,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vibrava.Name",
    family_id=328,
    abilities=[
        Ability(
            title="Dragon Guard",
            game_text="Prevent all effects of your opponent's attacks, except damage, done to your Dragon Pok\u00e9mon. (Existing effects are not removed.)",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=dragon_guard_passive,
        ),
        Attack(
            title="Sand Tomb",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=110,
            effect=condition_attack(no_retreat=True),
        ),
    ],
)