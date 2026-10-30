from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import fluffy_fur_asleep_on_damage, pester_sc_bonus
from spirit.game.card_effects.support_common import draw_attack


card = PokemonCardDef(
    guid="1d69548f-5da0-5be0-8686-513a88f82ad4",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wigglytuff.Name",
    display_name="Wigglytuff",
    searchable_by=["Wigglytuff", "Stage 1", "Wigglytuff"],
    subtypes=["Stage 1"],
    collector_number=13,
    set_code="EX14",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Jigglypuff.Name",
    family_id=39,
    abilities=[
        Ability(
            title="Fluffy Fur",
            game_text="If Wigglytuff is your Active Pok\u00e9mon and is damaged by an opponent's attack (even if Wigglytuff is Knocked Out), the Attacking Pok\u00e9mon is now Asleep.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=fluffy_fur_asleep_on_damage(),
            effect=None,
        ),
        Attack(
            title="Collect",
            game_text="Draw 3 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=draw_attack(3),
        ),
        Attack(
            title="Pester",
            game_text="If the Defending Pok\u00e9mon is affected by a Special Condition, this attack does 30 damage plus 20 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
                        effect=pester_sc_bonus(30, 30),
        ),
    ],
)