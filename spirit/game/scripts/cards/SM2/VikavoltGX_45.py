from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import attach_from_discard
from spirit.game.card_effects.attacks_common import self_energy_discard_attack
from spirit.game.card_effects.attacks_common import spread_damage


card = PokemonCardDef(
    guid="91af7bba-1441-5a27-a886-9f432890be7b",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.VikavoltGX.Name",
    display_name="Vikavolt-GX",
    searchable_by=["Vikavolt-GX", "Stage 2", "GX", "VikavoltGX"],
    subtypes=["Stage 2", "GX"],
    collector_number=45,
    set_code="SM2",
    rarity=Rarities.RareHoloGX,
    hp=240,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charjabug.Name",
    family_id=738,
    abilities=[
        Attack(
            title="Charge Beam",
            game_text="Attach an Energy card from your discard pile to this Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=50,
            effect=attach_from_discard(),
        ),
        Attack(
            title="Super Zap Cannon",
            game_text="Discard 2 Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 3},
            damage=180,
            effect=self_energy_discard_attack(count=2),
        ),
        Attack(
            title="Gigatron-GX",
            game_text="This attack does 60 damage to each of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 3},
            effect=spread_damage(60),
        ),
    ],
)