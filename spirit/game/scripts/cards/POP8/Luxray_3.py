"""Luxray (POP8 #3)."""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.ex import team_takes_less_before_wr


card = PokemonCardDef(
    guid="5a98bf51-849e-542f-87df-56d323b0f638",
    key="POP8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Luxray.Name",
    display_name="Luxray",
    searchable_by=["Luxray", "Stage 2", "Luxray"],
    subtypes=["Stage 2"],
    collector_number=3,
    set_code="POP8",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Luxio.Name",
    family_id=404,
    abilities=[
        Ability(
            title="Intimidating Fang",
            game_text="As long as Luxray is your Active Pok\u00e9mon, any damage done by an opponent's attack is reduced by 10 (before applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_BODY,
            passive=team_takes_less_before_wr(10),
        ),
        Attack(
            title="Thunder",
            game_text="Flip a coin. If tails, Luxray does 40 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 3, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=flip_damage(tails_self_damage=40),
        ),
    ],
)
