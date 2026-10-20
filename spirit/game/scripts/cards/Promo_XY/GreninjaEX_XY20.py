from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack, self_energy_discard_attack


card = PokemonCardDef(
    guid="3efc9b16-f922-5b95-b23c-47759843b5ca",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GreninjaEX.Name",
    display_name="Greninja-EX",
    searchable_by=["Greninja-EX", "Basic", "EX", "GreninjaEX"],
    subtypes=["Basic", "EX"],
    collector_number=20,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=170,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=658,
    abilities=[
        Attack(
            title="Sharpshooting",
            game_text="This attack does 30 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1},
            effect=snipe_attack(30, pool='any', count=1),
        ),
        Attack(
            title="Aqua Blast",
            game_text="Discard 1 Water Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=self_energy_discard_attack(count=1, energy_type=PokemonTypes.WATER),
        ),
    ],
)