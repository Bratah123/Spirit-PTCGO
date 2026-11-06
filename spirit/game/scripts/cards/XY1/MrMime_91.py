from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.support_common import heal_targets


card = PokemonCardDef(
    guid="d9bb3256-dff6-526f-b68b-eb88d4363ceb",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MrMime.Name",
    display_name="Mr. Mime",
    searchable_by=["Mr. Mime", "Basic", "MrMime"],
    subtypes=["Basic"],
    collector_number=91,
    set_code="XY1",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=122,
    abilities=[
        Attack(
            title="Massage",
            game_text="Heal 60 damage from 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 1},
            effect=heal_targets(60, 'bench_choice'),
        ),
        Attack(
            title="Slap Down",
            game_text="Flip 2 coins. This attack does 20 more damage for each heads.",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            effect=flip_damage(coins=2, bonus_per_heads=20),
        ),
    ],
)