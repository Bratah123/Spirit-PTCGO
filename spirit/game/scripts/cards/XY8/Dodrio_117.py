from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import retreat_discount, is_in_active_spot
from spirit.game.card_effects.attacks_common import flip_damage


card = PokemonCardDef(
    guid="92075c7f-085e-5fd2-99d8-4b80674ac635",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dodrio.Name",
    display_name="Dodrio",
    searchable_by=["Dodrio", "Stage 1", "Dodrio"],
    subtypes=["Stage 1"],
    collector_number=117,
    set_code="XY8",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Doduo.Name",
    family_id=84,
    abilities=[
        Ability(
            title="Retreat Aid",
            game_text="As long as this Pok\u00e9mon is on your Bench, your Active Pok\u00e9mon's Retreat Cost is ColorlessColorless less.",
            passive=retreat_discount(2, target_pred=lambda pokemon, carrier: pokemon.owning_player_id == carrier.owning_player_id and is_in_active_spot(pokemon) and (not is_in_active_spot(carrier))),
        ),
        Attack(
            title="Fury Attack",
            game_text="Flip 3 coins. This attack does 40 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            damage_operator="x",
            effect=flip_damage(3, per_heads=40),
        ),
    ],
)