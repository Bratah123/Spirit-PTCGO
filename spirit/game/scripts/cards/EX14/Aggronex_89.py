from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import intimidating_armor_basic_lock, mega_burn_self_lock, split_bomb_snipe

card = PokemonCardDef(
    guid="b285e3be-c871-59b6-951a-95fa48c9de93",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Aggronex.Name",
    display_name="Aggron ex",
    searchable_by=["Aggron ex", "Stage 2", "ex", "Aggronex"],
    subtypes=["Stage 2", "ex"],
    collector_number=89,
    set_code="EX14",
    rarity=Rarities.RareHoloEX,
    hp=150,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lairon.Name",
    family_id=304,
    abilities=[
        Ability(
            title="Intimidating Armor",
            game_text="As long as Aggron ex is your Active Pok\u00e9mon, your opponent's Basic Pok\u00e9mon can't attack or use any Pok\u00e9-Powers or Pok\u00e9-Bodies.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=intimidating_armor_basic_lock(),
            effect=None,
        ),
        Attack(
            title="Split Bomb",
            game_text="Choose 2 of your opponent's Pok\u00e9mon. This attack doe 30 damage to each of them. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 3},
                        effect=split_bomb_snipe(30, 2),
        ),
        Attack(
            title="Mega Burn",
            locks_next_turn=True,
            game_text="During your next turn, Aggron ex can't use Mega Burn.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 2},
            damage=100,
                        effect=mega_burn_self_lock(),
        ),
    ],
)