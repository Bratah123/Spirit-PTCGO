from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, damage_counters_on
from spirit.game.card_effects.attacks_common import damage_per, damage_counters_on


card = PokemonCardDef(
    guid="9c5f2ee9-cbc9-52dd-82a3-e99891a090b0",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TaurosGX.Name",
    display_name="Tauros-GX",
    searchable_by=["Tauros-GX", "Basic", "GX", "TaurosGX"],
    subtypes=["Basic", "GX"],
    collector_number=156,
    set_code="SM1",
    rarity=Rarities.RareRainbow,
    hp=180,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=128,
    abilities=[
        Attack(
            title="Rage",
            game_text="This attack does 10 more damage for each damage counter on this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            effect=damage_per(damage_counters_on('self'), 10, base=20),
        ),
        Attack(
            title="Horn Attack",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
        Attack(
            title="Mad Bull-GX",
            game_text="This attack does 30 damage for each damage counter on this Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="x",
            effect=damage_per(damage_counters_on('self'), 30),
        ),
    ],
)