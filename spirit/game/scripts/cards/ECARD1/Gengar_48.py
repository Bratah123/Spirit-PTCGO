from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.support_common import switch_self_attack
from spirit.game.card_effects.ecard import chaos_move, chaos_move_condition


card = PokemonCardDef(
    guid="a840f406-11ce-5b82-9d23-801af01c3de4",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gengar.Name",
    display_name="Gengar",
    searchable_by=["Gengar", "Stage 2", "Gengar"],
    subtypes=["Stage 2"],
    collector_number=48,
    set_code="ECARD1",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Haunter.Name",
    family_id=92,
    abilities=[
        Ability(
            title="Chaos Move",
            game_text="Once during your turn (before your attack), if your opponent has 3 or fewer Prizes, you may move 1 damage counter from 1 Pok\u00e9mon (yours or your opponent's) to another (even if it would Knock Out the other Pok\u00e9mon). This power can't be used if Gengar is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=chaos_move_condition,
            effect=chaos_move,
        ),
        Attack(
            title="Hide in Shadows",
            game_text="Switch Gengar with 1 of your Benched Pok\u00e9mon, if any.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=switch_self_attack(),
        ),
    ],
)
