from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.passives_common import attack_effect_shield_passive
from spirit.game.card_effects.ecard import drag_off


card = PokemonCardDef(
    guid="dd5166d0-6fe1-53ec-a313-2889df16c6ca",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Machamp.Name",
    display_name="Machamp",
    searchable_by=["Machamp", "Stage 2", "Machamp"],
    subtypes=["Stage 2"],
    collector_number=165,
    set_code="ECARD3",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Machoke.Name",
    family_id=66,
    abilities=[
        Ability(
            title="Immunity",
            game_text="Prevent all effects of your opponent's attacks done to Machamp.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=attack_effect_shield_passive(),
        ),
        Attack(
            title="Drag Off",
            game_text="Before doing damage, if your opponent has any Benched Pok\u00e9mon, choose 1 of them and switch it with the Defending Pok\u00e9mon. If your opponent has no Benched Pok\u00e9mon, ignore this effect.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=drag_off,
        ),
        Attack(
            title="Hurricane Punch",
            game_text="Flip 4 coins. This attack does 30 damage times the number of heads.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="x",
            effect=flip_damage(coins=4, per_heads=30),
        ),
    ],
)
