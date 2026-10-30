from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import count_energy, flip_damage
from spirit.game.card_effects.support_common import heal_attack


card = PokemonCardDef(
    guid="628bd3bb-a3c2-51b2-9409-2c432f057530",
    key="EX2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kabutopsex.Name",
    display_name="Kabutops ex",
    searchable_by=["Kabutops ex", "Stage 2", "ex", "Kabutopsex"],
    subtypes=["Stage 2", "ex"],
    collector_number=97,
    set_code="EX2",
    rarity=Rarities.RareHoloEX,
    hp=150,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Kabuto.Name",
    family_id=140,
    abilities=[
        Attack(
            title="Hydrocutter",
            game_text="Flip a number of coins equal to the amount of Energy attached to Kabutops ex. This attack does 40 damage times the number of heads. You can't flip more than 3 coins in this way.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator="x",
            effect=flip_damage(
                per_heads=40,
                coins_from=lambda ctx: min(3, count_energy("self")(ctx)),
            ),
        ),
        Attack(
            title="Spiral Drain",
            game_text="Remove 2 damage counters from Kabutops ex (remove 1 if there is only 1).",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=heal_attack(20),
        ),
    ],
)
