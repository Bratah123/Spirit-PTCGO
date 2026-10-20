from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import discard_opponent_energy_attack, flip_damage


card = PokemonCardDef(
    guid="a244dfda-ebc0-5225-922f-1487a3b98393",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cacturne.Name",
    display_name="Cacturne",
    searchable_by=["Cacturne", "Stage 1", "Cacturne"],
    subtypes=["Stage 1"],
    collector_number=88,
    set_code="XY8",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cacnea.Name",
    family_id=331,
    abilities=[
        Attack(
            title="Derail",
            game_text="Discard a Special Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=30,
            effect=discard_opponent_energy_attack(special_only=True),
        ),
        Attack(
            title="Pin Missile",
            game_text="Flip 3 coins. This attack does 40 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            damage_operator="x",
            effect=flip_damage(3, per_heads=40),
        ),
    ],
)