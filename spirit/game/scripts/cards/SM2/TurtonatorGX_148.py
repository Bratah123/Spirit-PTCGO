from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import self_energy_discard_attack
from spirit.game.scripts.cards.SM2.TurtonatorGX_18 import nitro_tank_gx
from spirit.game.scripts.cards.SWSH8.Turtonator_198 import shell_trap


card = PokemonCardDef(
    guid="d4252e86-e533-5fe5-8173-b7cf56ad51a3",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TurtonatorGX.Name",
    display_name="Turtonator-GX",
    searchable_by=["Turtonator-GX", "Basic", "GX", "TurtonatorGX"],
    subtypes=["Basic", "GX"],
    collector_number=148,
    set_code="SM2",
    rarity=Rarities.RareRainbow,
    hp=190,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    family_id=776,
    abilities=[
        Attack(
            title="Shell Trap",
            game_text="During your opponent's next turn, if this Pok\u00e9mon is damaged by an attack (even if this Pok\u00e9mon is Knocked Out), put 8 damage counters on the Attacking Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=shell_trap,
        ),
        Attack(
            title="Bright Flame",
            game_text="Discard 2 Fire Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=self_energy_discard_attack(count=2, energy_type=PokemonTypes.FIRE),
        ),
        Attack(
            title="Nitro Tank-GX",
            game_text="Attach 5 Fire Energy cards from your discard pile to your Pok\u00e9mon in any way you like. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIRE: 1},
            effect=nitro_tank_gx,
        ),
    ],
)