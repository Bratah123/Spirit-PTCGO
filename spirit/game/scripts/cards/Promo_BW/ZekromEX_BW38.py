from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus, self_energy_discard_attack


card = PokemonCardDef(
    guid="c89625ea-c496-5f04-8524-6ce669b4afa6",
    key="Promo_BW",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ZekromEX.Name",
    display_name="Zekrom-EX",
    searchable_by=["Zekrom-EX", "Basic", "EX", "ZekromEX"],
    subtypes=["Basic", "EX"],
    collector_number=38,
    set_code="Promo_BW",
    rarity=Rarities.RarePromo,
    hp=180,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=644,
    abilities=[
        Attack(
            title="Glinting Claw",
            game_text="Flip a coin. If heads, this attack does 30 more damage.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=flip_bonus(30),
        ),
        Attack(
            title="Strong Volt",
            game_text="Discard 2 Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 2},
            damage=150,
            effect=self_energy_discard_attack(count=2),
        ),
    ],
)