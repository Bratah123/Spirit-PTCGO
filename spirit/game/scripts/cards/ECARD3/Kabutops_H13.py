from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.ecard import PrimalAuraPassive


card = PokemonCardDef(
    guid="4d8a0889-82c0-57c0-9105-08b13e4e73ab",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kabutops.Name",
    display_name="Kabutops",
    searchable_by=["Kabutops", "Stage 2", "Kabutops"],
    subtypes=["Stage 2"],
    collector_number=163,
    set_code="ECARD3",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Kabuto.Name",
    family_id=140,
    abilities=[
        Ability(
            title="Primal Aura",
            game_text="As long as Kabutops is your Active Pok\u00e9mon, neither player can play Basic Pok\u00e9mon or Evolution cards from his or her hand to evolve Benched Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=PrimalAuraPassive(),
        ),
        Attack(
            title="Dual Cut",
            game_text="Flip 2 coins. This attack does 50 damage times the number of heads.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="x",
            effect=flip_damage(coins=2, per_heads=50),
        ),
    ],
)
