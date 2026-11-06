from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import flip_damage, self_energy_discard_attack
from spirit.game.card_effects.ecard import (
    CrystalTypePassive, crystal_type_on_energy_attached,
)


card = PokemonCardDef(
    guid="4ed4bbba-9387-55b3-9f25-068a44ff2ca8",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charizard.Name",
    display_name="Charizard",
    searchable_by=["Charizard", "Stage 2", "Charizard"],
    subtypes=["Stage 2"],
    collector_number=146,
    set_code="ECARD3",
    rarity=Rarities.RareSecret,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charmeleon.Name",
    family_id=6,
    abilities=[
        Ability(
            title="Crystal Type",
            game_text="Whenever you attach a Fire, Lightning, or Fighting basic Energy card from your hand to Charizard, Charizard's type (color) becomes the same as that type of Energy until the end of the turn.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=CrystalTypePassive(),
            trigger=Triggers.ON_ENERGY_ATTACHED,
            effect=crystal_type_on_energy_attached(
                PokemonTypes.FIRE, PokemonTypes.LIGHTNING, PokemonTypes.FIGHTING,
            ),
        ),
        Attack(
            title="Fireblast",
            game_text="Discard an Energy card attached to Charizard.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.FIGHTING: 1},
            damage=40,
            effect=self_energy_discard_attack(1),
        ),
        Attack(
            title="Dragon Tail",
            game_text="Flip 2 coins. This attack does 50 damage times the number of heads.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="x",
            effect=flip_damage(coins=2, per_heads=50),
        ),
    ],
)
